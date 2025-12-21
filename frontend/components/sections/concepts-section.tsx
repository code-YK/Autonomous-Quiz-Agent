import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Lightbulb, BookOpen } from "lucide-react"
import type { Concept } from "@/lib/types"

interface ConceptsSectionProps {
  concepts: Concept[]
}

export function ConceptsSection({ concepts }: ConceptsSectionProps) {
  return (
    <div className="space-y-4">
      <div className="flex items-center gap-2 mb-4">
        <Lightbulb className="h-5 w-5 text-primary" />
        <h3 className="text-lg font-semibold text-foreground">
          Extracted Concepts ({concepts.length})
        </h3>
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        {concepts.map((concept, index) => (
          <Card
            key={index}
            className="border-border hover:border-primary/50 transition-colors"
          >
            <CardHeader className="pb-3">
              <CardTitle className="text-base">
                {concept.name}
              </CardTitle>
            </CardHeader>

            <CardContent className="space-y-2">
              {/* Primary description */}
              <CardDescription className="text-sm leading-relaxed">
                {concept.description}
              </CardDescription>

              {/* Optional short summary */}
              {concept.summary && (
                <div className="flex gap-2 text-sm text-muted-foreground pt-2">
                  <BookOpen className="h-4 w-4 mt-0.5 text-primary" />
                  <p className="leading-relaxed">
                    {concept.summary}
                  </p>
                </div>
              )}
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  )
}

