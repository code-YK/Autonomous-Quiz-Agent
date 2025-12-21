"use client"

import { useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Network, ChevronDown, ChevronUp } from "lucide-react"

interface HierarchySectionProps {
  hierarchy: unknown
}

export function HierarchySection({ hierarchy }: HierarchySectionProps) {
  const [isExpanded, setIsExpanded] = useState(false)

  return (
    <div className="space-y-4">
      <div className="flex items-center gap-2 mb-4">
        <Network className="h-5 w-5 text-primary" />
        <h3 className="text-lg font-semibold text-foreground">Knowledge Hierarchy</h3>
      </div>

      <Card className="border-border">
        <CardHeader>
          <div className="flex items-center justify-between">
            <div>
              <CardTitle className="text-base">Concept Organization</CardTitle>
              <CardDescription>Hierarchical structure of concepts and their relationships</CardDescription>
            </div>
            <Button variant="ghost" size="sm" onClick={() => setIsExpanded(!isExpanded)}>
              {isExpanded ? (
                <>
                  <ChevronUp className="h-4 w-4 mr-1" />
                  Collapse
                </>
              ) : (
                <>
                  <ChevronDown className="h-4 w-4 mr-1" />
                  Expand
                </>
              )}
            </Button>
          </div>
        </CardHeader>
        <CardContent>
          <div className={`${isExpanded ? "" : "max-h-[400px]"} overflow-auto`}>
            <pre className="text-xs font-mono bg-muted/50 p-4 rounded-lg overflow-x-auto">
              {JSON.stringify(hierarchy, null, 2)}
            </pre>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
