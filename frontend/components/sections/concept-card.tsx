import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

interface ConceptCardProps {
  name: string
  description: string
}

export function ConceptCard({ name, description }: ConceptCardProps) {
  return (
    <Card className="bg-card/50 backdrop-blur border-border">
      <CardHeader>
        <CardTitle className="text-lg font-semibold">
          {name}
        </CardTitle>
      </CardHeader>

      <CardContent>
        <p className="text-sm text-muted-foreground">
          {description}
        </p>
      </CardContent>
    </Card>
  )
}
